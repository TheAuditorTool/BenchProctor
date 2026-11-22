const express = require("express");
const session = require("express-session");

const authorizePayment = require("./payment_authorize").authorizePayment;
const annotateSnapshot = require("./annotate_snapshot").annotateSnapshot;
const auditReport = require("./audit_report").auditReport;
const buildPayout = require("./build_payout").buildPayout;
const fetchRecord = require("./fetch_record").fetchRecord;
const reconcileDispute = require("./reconcile_dispute").reconcileDispute;
const fetchProfile = require("./fetch_profile").fetchProfile;
const buildDispute = require("./build_dispute").buildDispute;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/authorizePayment", authorizePayment);
app.post("/annotateSnapshot", annotateSnapshot);
app.post("/auditReport", auditReport);
app.post("/buildPayout", buildPayout);
app.post("/fetchRecord", fetchRecord);
app.post("/reconcileDispute", reconcileDispute);
app.post("/fetchProfile", fetchProfile);
app.post("/buildDispute", buildDispute);

app.listen(3000, "0.0.0.0");
