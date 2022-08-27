import os
import shutil
import time


while True:
    folder_path = r"C:\Users\Winter Hardcastle\Downloads/"
    folder_list = os.listdir(folder_path)

    extension_dict = {
        "3D Objects": ".obj.stl.step.fbx.3dmf.3mf.b3d.blend.block.dpm.g.glb.ma.max.mb.m.mesh.mm3d.off.rwx.sldasm.sldprt.u3d.wrl.vue.vwc.w3d.x.x3d",
        "Videos": ".mp4.mov.wmv.avi.flv.webm.mpeg-2.avchd.mpeg",
        "Photos": ".jpeg.jpg.gif.png.tiff.psd.ai.raw.heic",
        "Documents": ".pdf.docx.doc.docm.html.txt.rtf.xml.odt",
        "Executables": ".exe.bat.bin.cmd.msi.img",
        "Vectors": ".svg.dxf.dwf.emf.dwg.pwj5",
        "Zip": ".zip.zipx",
        "GCODE": ".gcode.makerbot.x3g",
    }

    def sorter(file):
        file_name, file_extension = os.path.splitext(folder_path + file)

        dest_folder = "misc/"

        for key in extension_dict:

            file_extensions = str(extension_dict[key])

            if str(file_extension) in file_extensions:

                dest_folder = key

                try:
                    os.mkdir(folder_path + "/" + key)

                except FileExistsError:
                    pass

        # print(dest_folder)
        # print(folder_path + dest_folder + '/' + file)

        shutil.move(folder_path + file, folder_path + dest_folder + "/" + file)

        return 0

    blacklisted_folders = ["Folders", "Misc"]

    for key in extension_dict:
        blacklisted_folders.append(key)

    for f in folder_list:
        if not os.path.isdir(folder_path + f):
            sorter(f)
        else:
            if f not in blacklisted_folders:
                shutil.move(folder_path + f, folder_path + "Folders/" + f)

    time.sleep(600)
