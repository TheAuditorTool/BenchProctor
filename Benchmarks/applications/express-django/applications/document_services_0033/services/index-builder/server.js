const express = require("express");
const session = require("express-session");

const indexDocument = require("./search_index").indexDocument;
const rotateConversion = require("./rotate_conversion").rotateConversion;
const rotateSchedule = require("./rotate_schedule").rotateSchedule;
const publishSchedule = require("./publish_schedule").publishSchedule;
const enrichReceipt = require("./enrich_receipt").enrichReceipt;
const fetchRecord = require("./fetch_record").fetchRecord;
const renderThreshold = require("./render_threshold").renderThreshold;
const formatProfile = require("./format_profile").formatProfile;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/indexDocument", indexDocument);
app.post("/rotateConversion", rotateConversion);
app.post("/rotateSchedule/:id", rotateSchedule);
app.post("/publishSchedule", publishSchedule);
app.post("/enrichReceipt", enrichReceipt);
app.post("/fetchRecord", fetchRecord);
app.post("/renderThreshold", renderThreshold);
app.post("/formatProfile", formatProfile);

app.listen(3000, "0.0.0.0");
