const express = require("express");
const session = require("express-session");

const applyPromo = require("./promo_apply").applyPromo;
const loadWindow = require("./load_window").loadWindow;
const collectManifest = require("./collect_manifest").collectManifest;
const fetchSummary = require("./fetch_summary").fetchSummary;
const renderReport = require("./render_report").renderReport;
const auditLedger = require("./audit_ledger").auditLedger;
const publishSchedule = require("./publish_schedule").publishSchedule;
const fetchBatch = require("./fetch_batch").fetchBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/applyPromo", route(applyPromo));
app.post("/loadWindow", route(loadWindow));
app.post("/collectManifest", route(collectManifest));
app.post("/fetchSummary", route(fetchSummary));
app.post("/renderReport", route(renderReport));
app.post("/auditLedger", route(auditLedger));
app.post("/publishSchedule", route(publishSchedule));
app.post("/fetchBatch", route(fetchBatch));

app.listen(3000, "0.0.0.0");
