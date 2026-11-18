const express = require("express");
const session = require("express-session");

const submitInvoice = require("./invoice_intake").submitInvoice;
const verifyLedger = require("./verify_ledger").verifyLedger;
const rotateInvoice = require("./rotate_invoice").rotateInvoice;
const renderProfile = require("./render_profile").renderProfile;
const archiveReport = require("./archive_report").archiveReport;
const normalizeSchedule = require("./normalize_schedule").normalizeSchedule;
const resolveSnapshot = require("./resolve_snapshot").resolveSnapshot;
const compactReceipt = require("./compact_receipt").compactReceipt;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/submitInvoice", route(submitInvoice));
app.post("/verifyLedger", route(verifyLedger));
app.post("/rotateInvoice/:id", route(rotateInvoice));
app.post("/renderProfile", route(renderProfile));
app.post("/archiveReport", route(archiveReport));
app.post("/normalizeSchedule", route(normalizeSchedule));
app.post("/resolveSnapshot", route(resolveSnapshot));
app.post("/compactReceipt", route(compactReceipt));

app.listen(3000, "0.0.0.0");
