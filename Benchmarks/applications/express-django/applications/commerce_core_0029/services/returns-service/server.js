const express = require("express");
const session = require("express-session");

const requestReturn = require("./return_request").requestReturn;
const archiveWindow = require("./archive_window").archiveWindow;
const normalizeCheckpoint = require("./normalize_checkpoint").normalizeCheckpoint;
const resolveWindow = require("./resolve_window").resolveWindow;
const renderSummary = require("./render_summary").renderSummary;
const loadBundle = require("./load_bundle").loadBundle;
const mergeProfile = require("./merge_profile").mergeProfile;
const buildWindow = require("./build_window").buildWindow;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/requestReturn", route(requestReturn));
app.post("/archiveWindow", route(archiveWindow));
app.post("/normalizeCheckpoint", route(normalizeCheckpoint));
app.post("/resolveWindow", route(resolveWindow));
app.post("/renderSummary", route(renderSummary));
app.post("/loadBundle", route(loadBundle));
app.post("/mergeProfile", route(mergeProfile));
app.post("/buildWindow", route(buildWindow));

app.listen(3000, "0.0.0.0");
