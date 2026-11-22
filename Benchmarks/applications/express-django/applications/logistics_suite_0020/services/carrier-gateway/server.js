const express = require("express");
const session = require("express-session");

const dispatchCarrier = require("./carrier_dispatch").dispatchCarrier;
const renderRoster = require("./render_roster").renderRoster;
const formatReceipt = require("./format_receipt").formatReceipt;
const rotateWaybill = require("./rotate_waybill").rotateWaybill;
const pruneSummary = require("./prune_summary").pruneSummary;
const publishPolicy = require("./publish_policy").publishPolicy;
const verifyBundle = require("./verify_bundle").verifyBundle;
const validateSummary = require("./validate_summary").validateSummary;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/dispatchCarrier", dispatchCarrier);
app.post("/renderRoster", renderRoster);
app.post("/formatReceipt", formatReceipt);
app.post("/rotateWaybill", rotateWaybill);
app.post("/pruneSummary", pruneSummary);
app.post("/publishPolicy", publishPolicy);
app.post("/verifyBundle", verifyBundle);
app.post("/validateSummary", validateSummary);

app.listen(3000, "0.0.0.0");
