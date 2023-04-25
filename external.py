import dearpygui.dearpygui as gui
import pymem

#Defaults variables
sv_cheats = 0
drawmodels = 1
game = ""

#Game selection
def game_selection(sender, data):
    global pm
    global client
    global engine
    global sv_cheatsaddress
    global r_drawothermodelsaddress
    game = gui.get_value(sender)
    if game == "TF2":
        pm = pymem.Pymem('hl2.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #TF2 Address
        sv_cheatsaddress = 0x606160
        r_drawothermodelsaddress = 0xC44540

        gui.show_item("ShowGameTab")
        gui.set_item_label("ShowGameTab", game)
        gui.disable_item("SelectGameCombo")

    if game == "CS:GO":
        pm = pymem.Pymem('csgo.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #CSGO Address
        sv_cheatsaddress = 0x5A4268
        r_drawothermodelsaddress = 0xDE5648

        gui.show_item("ShowGameTab")
        gui.set_item_label("ShowGameTab", game)
        gui.disable_item("SelectGameCombo")

    if game == "CSS":
        pm = pymem.Pymem('hl2.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #CSS Address
        sv_cheatsaddress = 0x616A70
        r_drawothermodelsaddress = 0x4C4BA0

        gui.show_item("ShowGameTab")
        gui.set_item_label("ShowGameTab", game)
        gui.disable_item("SelectGameCombo")

    if game == "GMOD (default branch)":
        pm = pymem.Pymem('hl2.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #GMOD Address
        sv_cheatsaddress = 0x69B6A8
        r_drawothermodelsaddress = 0x6EB2A0

        gui.show_item("ShowGameTab")
        gui.set_item_label("ShowGameTab", game)
        gui.disable_item("SelectGameCombo")

    if game == "L4D2":
        pm = pymem.Pymem('left4dead2.exe')
        client = 0
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #L4D2 Address
        sv_cheatsaddress = 0x6719A0
        r_drawothermodelsaddress = 0x7B110768

        gui.show_item("ShowGameTab")
        gui.set_item_label("ShowGameTab", game)
        gui.disable_item("SelectGameCombo")


#Checkbox sv_cheats
def checkbox_svcheats(sender, data):
    global sv_cheats
    SVC = pm.read_uint(engine + sv_cheatsaddress)
    if sv_cheats == 0:
        sv_cheats = 1
        pm.write_uint(engine + sv_cheatsaddress, SVC+1)
    else:
        sv_cheats = 0
        pm.write_uint(engine + sv_cheatsaddress, SVC-1)

#Checkbox for usefull commands
def checkbox_drawmodels(sender, data):
    global drawmodels
    DOM = pm.read_uint(client + r_drawothermodelsaddress)
    if drawmodels == 1:
        drawmodels = 2
        pm.write_uint(client + r_drawothermodelsaddress, DOM+1)
    else:
        drawmodels = 1
        pm.write_uint(client + r_drawothermodelsaddress, DOM-1)
        

#Interface
gui.create_context()
gui.create_viewport(title='External sv_cheats Bypass', width=350, height=350)
gui.set_viewport_resizable(False)
gui.setup_dearpygui()
gui.set_viewport_always_top(True)

with gui.window(label='Nexus', width=350, height=400, no_title_bar=True, no_resize=True, no_move=True):
    with gui.tab_bar(label='Tabs'):

        with gui.tab(label='Game Selection'):
            gui.add_text("Select the game :")
            gui.add_text("(The game must already be launched)")
            gui.add_combo(("CS:GO", "GMOD (default branch)", "TF2", "CSS", "L4D2"), callback=game_selection, tag="SelectGameCombo")

        with gui.tab(label=game, show=False, tag="ShowGameTab"):
            gui.add_checkbox(label='sv_cheats', callback=checkbox_svcheats)
            gui.add_text("")
            with gui.collapsing_header(label="Useful commands"):
                gui.add_checkbox(label='r_drawothermodels', callback=checkbox_drawmodels)

        with gui.tab(label="About"):
            gui.add_text("Version : 1.0.1")
            gui.add_text("GitHub Page : github.com/Calvineries/External-sv_cheats-Bypass")
            gui.add_text("")
            gui.add_text("Author : Calvineries")
            gui.add_text("Contributors: ...")
gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()
