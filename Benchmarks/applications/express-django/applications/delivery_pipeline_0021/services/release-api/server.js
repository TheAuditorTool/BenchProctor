const express = require("express");
const session = require("express-session");

const cutRelease = require("./release_cut").cutRelease;
const publishSnapshot = require("./publish_snapshot").publishSnapshot;
const mergeWindow = require("./merge_window").mergeWindow;
const enrichPolicy = require("./enrich_policy").enrichPolicy;
const mergeHeader = require("./merge_header").mergeHeader;
const publishWindow = require("./publish_window").publishWindow;
const buildIndex = require("./build_index").buildIndex;
const loadPolicy = require("./load_policy").loadPolicy;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/cutRelease", route(cutRelease));
app.post("/publishSnapshot", route(publishSnapshot));
app.post("/mergeWindow", route(mergeWindow));
app.post("/enrichPolicy", route(enrichPolicy));
app.post("/mergeHeader", route(mergeHeader));
app.post("/publishWindow", route(publishWindow));
app.post("/buildIndex", route(buildIndex));
app.post("/loadPolicy", route(loadPolicy));

app.listen(3000, "0.0.0.0");
