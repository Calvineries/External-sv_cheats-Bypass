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

    gui.show_item("ShowGameTab")
    gui.set_item_label("ShowGameTab", game)
    gui.disable_item("SelectGameCombo")

    if game == "TF2":
        pm = pymem.Pymem('hl2.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #TF2 Address
        sv_cheatsaddress = 0x606160
        r_drawothermodelsaddress = 0xC44540

    if game == "CS:GO":
        pm = pymem.Pymem('csgo.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #CSGO Address
        sv_cheatsaddress = 0x5A4268
        r_drawothermodelsaddress = 0xDE5670

    if game == "CSS":
        pm = pymem.Pymem('hl2.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #CSS Address
        sv_cheatsaddress = 0x616A70
        r_drawothermodelsaddress = 0x4C4BA0

    if game == "GMOD (default branch)":
        pm = pymem.Pymem('hl2.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #GMOD Address
        sv_cheatsaddress = 0x69B6A8
        r_drawothermodelsaddress = 0x6EC320
        
    if game == "GMOD (x64)":
        pm = pymem.Pymem('gmod.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #GMOD x64 Address
        sv_cheatsaddress = 0x7BD318
        r_drawothermodelsaddress = 0x83A998

    if game == "L4D2":
        pm = pymem.Pymem('left4dead2.exe')
        client = 0
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #L4D2 Address
        sv_cheatsaddress = 0x6719A0
        r_drawothermodelsaddress = 0x7B110768

    if game == "L4D1":
        pm = pymem.Pymem('left4dead.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #L4D1 Address
        sv_cheatsaddress = 0x576178
        r_drawothermodelsaddress = 0x53C8C8

    if game == "DODS":
        pm = pymem.Pymem('hl2.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #Day Of Defeat Source Address
        sv_cheatsaddress = 0x616A70
        r_drawothermodelsaddress = 0x4A0C20

    if game == "Portal2":
        pm = pymem.Pymem('portal2.exe')
        client = pymem.pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll
        engine = pymem.pymem.process.module_from_name(pm.process_handle, 'engine.dll').lpBaseOfDll
        #Portal2 Address
        sv_cheatsaddress = 0x66B778
        r_drawothermodelsaddress = 0x9962C8


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
gui.create_viewport(title='External sv_cheats Bypass', decorated=True, width=370, height=400)
gui.set_viewport_resizable(False)
gui.setup_dearpygui()
gui.set_viewport_always_top(True)

with gui.window(label='Nexus', width=370, height=400, no_title_bar=True, no_resize=True, no_move=True):
    with gui.tab_bar(label='Tabs'):

        with gui.tab(label='Game Selection'):
            gui.add_text("Select the game :")
            gui.add_text("(The game must already be launched)")
            gui.add_combo(("CS:GO", "GMOD (default branch)", "GMOD (x64)", "TF2", "CSS", "L4D2", "L4D1", "DODS", "Portal2"), callback=game_selection, tag="SelectGameCombo")

        with gui.tab(label=game, show=False, tag="ShowGameTab"):
            gui.add_checkbox(label='sv_cheats', callback=checkbox_svcheats)
            gui.add_text("")
            with gui.collapsing_header(label="Useful commands"):
                gui.add_checkbox(label='r_drawothermodels', callback=checkbox_drawmodels)

        with gui.tab(label="About"):
            gui.add_text("Version : 1.0.7")
            # https://github.com/Calvineries/External-sv_cheats-Bypass
            gui.add_text("GitHub Page : github.com/Calvineries\n/External-sv_cheats-Bypass")            
            gui.add_text("")
            gui.add_text("Author : Calvineries")
            gui.add_text("Contributors: ...")
gui.show_viewport()
gui.start_dearpygui()
gui.destroy_context()
