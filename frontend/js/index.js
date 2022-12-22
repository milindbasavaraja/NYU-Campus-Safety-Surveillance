const apigClient = apigClientFactory.newClient({
  apiKey: "SFAKBreHZt8ZhohvzmbeI5kx4W3xKLw35xOR19sy",
});

function uploadVideo() {
  let filePath = document.getElementById("image-file").value.split("\\");
  let fileName = filePath[filePath.length - 1];
  console.log("The file path is", filePath, "and file name is ", fileName);

  let reader = new FileReader();
  console.log(
    "The file object is:",
    document.getElementById("image-file").files[0]
  );
  let file = document.getElementById("image-file").files[0];
  console.log("The file is: ", file);
  document.getElementById("image-file").value = "";
  let params;

  params = {
    filename: file.name,
    key: file.name,
    bucket: "my-video-bucket-monitoring",
    "Content-Type": file.type,
    "x-api-key": "SFAKBreHZt8ZhohvzmbeI5kx4W3xKLw35xOR19sy",
  };

  console.log("Adding headers");
  let additionalParams = {
    headers: {
      ...params,
      Accept: "video/*",
      "Content-Type": file.type,
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "*",
      "Access-Control-Allow-Methods": "OPTIONS,PUT",
    },
  };

  console.log("The additional params is:", additionalParams);

  url =
    "https://zuowrlgrv9.execute-api.us-east-1.amazonaws.com/dev/upload/my-video-bucket-monitoring/" +
    file.name;
  axios.put(url, file, additionalParams).then((response) => {
    console.log(" New " + response.data);
    console.log("Success");
    // document.getElementById("uploadText").innerHTML =
    //   "Video UPLOADED SUCCESSFULLY!";
    // document.getElementById("uploadText").style.display = "block";
    // document.getElementById("uploadText").style.color = "white";
    // document.getElementById("uploadText").style.fontWeight = "bold";
  });
}

function startStreamProcessor() {
  const streamButtonElement = document.getElementById("start-stream");

  params = {
    "Content-Type": "applcation/json",
    "x-api-key": "SFAKBreHZt8ZhohvzmbeI5kx4W3xKLw35xOR19sy",
  };

  console.log("Adding headers");
  let additionalParams = {
    headers: {
      ...params,
      
      "Content-Type": "applcation/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Headers": "*",
      "Access-Control-Allow-Methods": "OPTIONS,POST",
    },
  };

  console.log(streamButtonElement.innerHTML === "Start Live Video Processing");
  if (streamButtonElement.innerHTML === "Start Live Video Processing") {
    streamButtonElement.innerHTML = "Stop Live Video Processing";
    url =
    "https://zuowrlgrv9.execute-api.us-east-1.amazonaws.com/dev/start-stream-processor"
    axios.post(url,additionalParams).then((response) => {
      console.log(" New " + response.data);
      console.log("Success");
    });
  } else {
    streamButtonElement.innerHTML = "Start Live Video Processing";
    url =
    "https://zuowrlgrv9.execute-api.us-east-1.amazonaws.com/dev/stop-stream-processor"
    axios.post(url,additionalParams).then((response) => {
      console.log(" New " + response.data);
      console.log("Success");
    });
  }
}
