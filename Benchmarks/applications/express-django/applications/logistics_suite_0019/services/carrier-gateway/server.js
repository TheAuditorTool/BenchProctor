const express = require("express");
const session = require("express-session");

const dispatchCarrier = require("./carrier_dispatch").dispatchCarrier;
const summarizeShipment = require("./summarize_shipment").summarizeShipment;
const compactSchedule = require("./compact_schedule").compactSchedule;
const collectThreshold = require("./collect_threshold").collectThreshold;
const mergeRoster = require("./merge_roster").mergeRoster;
const loadPolicy = require("./load_policy").loadPolicy;
const verifyPolicy = require("./verify_policy").verifyPolicy;
const fetchRoster = require("./fetch_roster").fetchRoster;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/dispatchCarrier", dispatchCarrier);
app.post("/summarizeShipment", summarizeShipment);
app.post("/compactSchedule", compactSchedule);
app.post("/collectThreshold", collectThreshold);
app.post("/mergeRoster", mergeRoster);
app.post("/loadPolicy", loadPolicy);
app.post("/verifyPolicy", verifyPolicy);
app.post("/fetchRoster", fetchRoster);

app.listen(3000, "0.0.0.0");
