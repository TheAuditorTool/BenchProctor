const express = require("express");
const session = require("express-session");

const settleCapture = require("./capture_settle").settleCapture;
const formatReport = require("./format_report").formatReport;
const collectHeader = require("./collect_header").collectHeader;
const annotateManifest = require("./annotate_manifest").annotateManifest;
const fetchProfile = require("./fetch_profile").fetchProfile;
const reconcileSummary = require("./reconcile_summary").reconcileSummary;
const summarizeProfile = require("./summarize_profile").summarizeProfile;
const buildHeader = require("./build_header").buildHeader;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/settleCapture", route(settleCapture));
app.post("/formatReport", route(formatReport));
app.post("/collectHeader", route(collectHeader));
app.post("/annotateManifest", route(annotateManifest));
app.post("/fetchProfile", route(fetchProfile));
app.post("/reconcileSummary/:id", route(reconcileSummary));
app.post("/summarizeProfile", route(summarizeProfile));
app.post("/buildHeader", route(buildHeader));

app.listen(3000, "0.0.0.0");
