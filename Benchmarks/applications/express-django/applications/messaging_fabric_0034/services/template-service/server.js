const express = require("express");
const session = require("express-session");

const composeTemplate = require("./template_compose").composeTemplate;
const compactSchedule = require("./compact_schedule").compactSchedule;
const summarizeSnapshot = require("./summarize_snapshot").summarizeSnapshot;
const resolveManifest = require("./resolve_manifest").resolveManifest;
const archiveSummary = require("./archive_summary").archiveSummary;
const auditSummary = require("./audit_summary").auditSummary;
const verifyBundle = require("./verify_bundle").verifyBundle;
const compactIndex = require("./compact_index").compactIndex;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/composeTemplate", route(composeTemplate));
app.post("/compactSchedule", route(compactSchedule));
app.post("/summarizeSnapshot", route(summarizeSnapshot));
app.post("/resolveManifest", route(resolveManifest));
app.post("/archiveSummary", route(archiveSummary));
app.post("/auditSummary", route(auditSummary));
app.post("/verifyBundle", route(verifyBundle));
app.post("/compactIndex", route(compactIndex));

app.listen(3000, "0.0.0.0");
