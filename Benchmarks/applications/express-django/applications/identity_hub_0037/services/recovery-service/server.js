const express = require("express");
const session = require("express-session");

const startRecovery = require("./recovery_start").startRecovery;
const verifyBatch = require("./verify_batch").verifyBatch;
const auditReport = require("./audit_report").auditReport;
const loadPolicy = require("./load_policy").loadPolicy;
const validateLedger = require("./validate_ledger").validateLedger;
const buildWindow = require("./build_window").buildWindow;
const archiveReceipt = require("./archive_receipt").archiveReceipt;
const rotateSummary = require("./rotate_summary").rotateSummary;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/startRecovery", route(startRecovery));
app.post("/verifyBatch", route(verifyBatch));
app.post("/auditReport", route(auditReport));
app.post("/loadPolicy", route(loadPolicy));
app.post("/validateLedger", route(validateLedger));
app.post("/buildWindow", route(buildWindow));
app.post("/archiveReceipt", route(archiveReceipt));
app.post("/rotateSummary", route(rotateSummary));

app.listen(3000, "0.0.0.0");
