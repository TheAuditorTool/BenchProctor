const express = require("express");
const session = require("express-session");

const updatePresence = require("./presence_update").updatePresence;
const verifyHeader = require("./verify_header").verifyHeader;
const exportRoster = require("./export_roster").exportRoster;
const annotateReceipt = require("./annotate_receipt").annotateReceipt;
const collectSchedule = require("./collect_schedule").collectSchedule;
const compactSchedule = require("./compact_schedule").compactSchedule;
const fetchRecord = require("./fetch_record").fetchRecord;
const auditSchedule = require("./audit_schedule").auditSchedule;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/updatePresence", route(updatePresence));
app.post("/verifyHeader", route(verifyHeader));
app.post("/exportRoster", route(exportRoster));
app.post("/annotateReceipt", route(annotateReceipt));
app.post("/collectSchedule", route(collectSchedule));
app.post("/compactSchedule", route(compactSchedule));
app.post("/fetchRecord", route(fetchRecord));
app.post("/auditSchedule", route(auditSchedule));

app.listen(3000, "0.0.0.0");
