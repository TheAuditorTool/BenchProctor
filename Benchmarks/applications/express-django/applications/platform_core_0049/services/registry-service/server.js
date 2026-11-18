const express = require("express");
const session = require("express-session");

const registerService = require("./service_register").registerService;
const verifySchedule = require("./verify_schedule").verifySchedule;
const verifyReceipt = require("./verify_receipt").verifyReceipt;
const validateHeader = require("./validate_header").validateHeader;
const buildLedger = require("./build_ledger").buildLedger;
const collectProfile = require("./collect_profile").collectProfile;
const exportConfig = require("./export_config").exportConfig;
const buildReport = require("./build_report").buildReport;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/registerService", route(registerService));
app.post("/verifySchedule/:id", route(verifySchedule));
app.post("/verifyReceipt", route(verifyReceipt));
app.post("/validateHeader", route(validateHeader));
app.post("/buildLedger", route(buildLedger));
app.post("/collectProfile", route(collectProfile));
app.post("/exportConfig", route(exportConfig));
app.post("/buildReport", route(buildReport));

app.listen(3000, "0.0.0.0");
