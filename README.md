# 3D-Screen-Illusion
This is code that was created to compete in the TSA Software Development Competition. I saw an article about Google's new screen that made video look 3D by tracking the user's face and moving the video based on their head movements. I thought it might be possible to get this same result on a normal laptop by using the Mediapipe face tracking code (https://google.github.io/mediapipe/solutions/face_mesh.html) to move a Blender scene based on where I was in the frame. The challenging part of the project was getting the Mediapipe code to interact with Blender at a convincing frame rate. Because they both relied on different Python versions, I ended up using socket communication to send the data to Blender which then and angled the camera. 
ㅤ
Process:
ㅤ
![unnamed (1)](https://github.com/NoahBSchwartz/3D-Screen-Illusion/assets/44248582/aa768b78-3afc-43e2-9aa0-c05c6392af67)
ㅤㅤㅤㅤㅤ
![unnamed](https://github.com/NoahBSchwartz/3D-Screen-Illusion/assets/44248582/054dbea0-516c-42d0-94dc-0b7e4efcdcaa)
ㅤㅤㅤㅤㅤ
![unnamed (2)](https://github.com/NoahBSchwartz/3D-Screen-Illusion/assets/44248582/5ddadec2-3c3f-4239-b3b5-2ff5bb0fe103)
