const express = require("express");
const session = require("express-session");

const declareCustoms = require("./customs_declare").declareCustoms;
const mergeShipment = require("./merge_shipment").mergeShipment;
const renderProfile = require("./render_profile").renderProfile;
const renderLedger = require("./render_ledger").renderLedger;
const validateCheckpoint = require("./validate_checkpoint").validateCheckpoint;
const renderWaybill = require("./render_waybill").renderWaybill;
const mergeRoster = require("./merge_roster").mergeRoster;
const reconcileSummary = require("./reconcile_summary").reconcileSummary;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/declareCustoms", route(declareCustoms));
app.post("/mergeShipment", route(mergeShipment));
app.post("/renderProfile", route(renderProfile));
app.post("/renderLedger", route(renderLedger));
app.post("/validateCheckpoint", route(validateCheckpoint));
app.post("/renderWaybill", route(renderWaybill));
app.post("/mergeRoster", route(mergeRoster));
app.post("/reconcileSummary", route(reconcileSummary));

app.listen(3000, "0.0.0.0");
