const express = require("express");
const session = require("express-session");

const declareCustoms = require("./customs_declare").declareCustoms;
const auditReport = require("./audit_report").auditReport;
const reconcileCheckpoint = require("./reconcile_checkpoint").reconcileCheckpoint;
const archiveDigest = require("./archive_digest").archiveDigest;
const publishWindow = require("./publish_window").publishWindow;
const publishSchedule = require("./publish_schedule").publishSchedule;
const publishWaybill = require("./publish_waybill").publishWaybill;
const summarizeLedger = require("./summarize_ledger").summarizeLedger;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/declareCustoms", route(declareCustoms));
app.post("/auditReport", route(auditReport));
app.post("/reconcileCheckpoint", route(reconcileCheckpoint));
app.post("/archiveDigest", route(archiveDigest));
app.post("/publishWindow", route(publishWindow));
app.post("/publishSchedule/:id", route(publishSchedule));
app.post("/publishWaybill/:id", route(publishWaybill));
app.post("/summarizeLedger", route(summarizeLedger));

app.listen(3000, "0.0.0.0");
