const express = require("express");
const session = require("express-session");

const openCase = require("./case_open").openCase;
const fetchCase = require("./fetch_case").fetchCase;
const buildSummary = require("./build_summary").buildSummary;
const rotateScreening = require("./rotate_screening").rotateScreening;
const reconcileThreshold = require("./reconcile_threshold").reconcileThreshold;
const loadIndex = require("./load_index").loadIndex;
const collectRecord = require("./collect_record").collectRecord;
const validateDigest = require("./validate_digest").validateDigest;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/openCase", route(openCase));
app.post("/fetchCase", route(fetchCase));
app.post("/buildSummary", route(buildSummary));
app.post("/rotateScreening", route(rotateScreening));
app.post("/reconcileThreshold", route(reconcileThreshold));
app.post("/loadIndex", route(loadIndex));
app.post("/collectRecord", route(collectRecord));
app.post("/validateDigest", route(validateDigest));

app.listen(3000, "0.0.0.0");
