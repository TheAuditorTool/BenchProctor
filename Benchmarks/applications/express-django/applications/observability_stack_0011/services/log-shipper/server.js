const express = require("express");
const session = require("express-session");

const shipLog = require("./log_ship").shipLog;
const loadSchedule = require("./load_schedule").loadSchedule;
const resolveWindow = require("./resolve_window").resolveWindow;
const verifyIndex = require("./verify_index").verifyIndex;
const normalizeAlert = require("./normalize_alert").normalizeAlert;
const loadThreshold = require("./load_threshold").loadThreshold;
const rotatePolicy = require("./rotate_policy").rotatePolicy;
const mergeSummary = require("./merge_summary").mergeSummary;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/shipLog", route(shipLog));
app.post("/loadSchedule", route(loadSchedule));
app.post("/resolveWindow", route(resolveWindow));
app.post("/verifyIndex", route(verifyIndex));
app.post("/normalizeAlert", route(normalizeAlert));
app.post("/loadThreshold", route(loadThreshold));
app.post("/rotatePolicy", route(rotatePolicy));
app.post("/mergeSummary", route(mergeSummary));

app.listen(3000, "0.0.0.0");
