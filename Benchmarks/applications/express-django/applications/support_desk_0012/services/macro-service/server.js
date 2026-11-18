const express = require("express");
const session = require("express-session");

const applyMacro = require("./macro_apply").applyMacro;
const compactBatch = require("./compact_batch").compactBatch;
const loadConfig = require("./load_config").loadConfig;
const normalizeRoster = require("./normalize_roster").normalizeRoster;
const mergeSummary = require("./merge_summary").mergeSummary;
const exportPolicy = require("./export_policy").exportPolicy;
const annotateReport = require("./annotate_report").annotateReport;
const fetchDigest = require("./fetch_digest").fetchDigest;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/applyMacro", route(applyMacro));
app.post("/compactBatch", route(compactBatch));
app.post("/loadConfig/:id", route(loadConfig));
app.post("/normalizeRoster", route(normalizeRoster));
app.post("/mergeSummary", route(mergeSummary));
app.post("/exportPolicy", route(exportPolicy));
app.post("/annotateReport", route(annotateReport));
app.post("/fetchDigest", route(fetchDigest));

app.listen(3000, "0.0.0.0");
