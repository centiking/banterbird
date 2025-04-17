const username = "admin";

function renderPost(post) {
    const template = document.getElementById("post-template").content.cloneNode(true);
    template.querySelector(".username").innerText = post.username;
    template.querySelector(".message").innerText = post.message;
    document.getElementById("feed").appendChild(template);
}

function submitPost() {
    const message = document.getElementById("postInput").value;
    const usernames = document.getElementById("username").value;
    renderPost({
        username: usernames,
        message: message,
    });
    console.log("Would post:", message);
    alert("Tweet submitted (not really yet)");
}

window.onload = () => {
    const hardcodedPost = {
        username: "admin",
        message: "Welcome to Banterbird! This post is hardcoded.",
    };
    renderPost(hardcodedPost);
};
