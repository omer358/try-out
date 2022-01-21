import os, shutil

episodes_titles = [
    "Uno","Mijo","Nacho","Hero","Alpine Shepherd Boy","Five-O","Bingo","Rico","Pimento","Marco",
        "Switch","Cobbler","Amarillo","Gloves Off","Rebecca","Bali Ha'i","Inflatable","Fifi","Nailed", "Klick"
        ,"Mabel","Witness","Sunk Costs","Sabrosito","Chicanery","Off Brand","Expenses","Slip","Fall", "Lantern"
        ,"Smoke","Breathe","Something Beautiful","Talk","Quite a Ride","Piñata","Something Stupid","Coushatta",
        "Wiedersehen", "Winner","Magic Man","50% Off","The Guy For This","Namaste","Dedicado a Max","Wexler v. Goodman","JMM","Bagman","Bad Choice Road", "Something Unforgivable"
        ]
#change to the path to where your Directory located
os.chdir('/home/omer358/Videos/Movies & Series/Series/Better Call Saul')
# A counter used to go through the episodes title list.
ep_title_count = 0
# Iterating through the current Directory and the subDirectory
for folderName, subfolders, filenames in sorted(os.walk('.')):
    # Iterating through each season Directory.
    for season in sorted(subfolders):
        # changing the dirctory to the season dirctory
        os.chdir(os.path.join(season))
        # This counter'll set to 1 for each new folder.
        ep_count = 1
        # Iterate through the episodes to change their names.
        for ep_name in sorted(os.listdir()):
            # format the new name.
            new_name = "Better_Call_Saul_{0}E{1}_{2}.mp4".format(
                        season,
                        ep_count,
                        episodes_titles[ep_title_count])
            # Print the new name                    
            print(shutil.move(ep_name,new_name))
            # Increase the counter by 1 
            ep_count = ep_count+1
            # increase the counter by 1 to go to the next title
            ep_title_count = ep_title_count+1
        # go back to the previous directory 
        os.chdir('..')