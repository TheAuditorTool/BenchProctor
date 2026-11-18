const express = require("express");
const session = require("express-session");

const recordConsent = require("./consent_record").recordConsent;
const annotateIndex = require("./annotate_index").annotateIndex;
const validateDevice = require("./validate_device").validateDevice;
const normalizeSnapshot = require("./normalize_snapshot").normalizeSnapshot;
const renderSummary = require("./render_summary").renderSummary;
const summarizeDevice = require("./summarize_device").summarizeDevice;
const auditThreshold = require("./audit_threshold").auditThreshold;
const verifyDevice = require("./verify_device").verifyDevice;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/recordConsent", route(recordConsent));
app.post("/annotateIndex/:id", route(annotateIndex));
app.post("/validateDevice/:id", route(validateDevice));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/renderSummary", route(renderSummary));
app.post("/summarizeDevice", route(summarizeDevice));
app.post("/auditThreshold", route(auditThreshold));
app.post("/verifyDevice", route(verifyDevice));

app.listen(3000, "0.0.0.0");
