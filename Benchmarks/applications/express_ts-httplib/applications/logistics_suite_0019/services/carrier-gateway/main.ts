import express, { Request, Response } from "express";
import session from "express-session";

import { dispatchCarrier } from "./carrier_dispatch";
import { summarizeShipment } from "./summarize_shipment";
import { compactSchedule } from "./compact_schedule";
import { collectThreshold } from "./collect_threshold";
import { mergeRoster } from "./merge_roster";
import { loadPolicy } from "./load_policy";
import { verifyPolicy } from "./verify_policy";
import { fetchRoster } from "./fetch_roster";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/dispatchCarrier", dispatchCarrier);
app.post("/summarizeShipment", summarizeShipment);
app.post("/compactSchedule", compactSchedule);
app.post("/collectThreshold", collectThreshold);
app.post("/mergeRoster", mergeRoster);
app.post("/loadPolicy", loadPolicy);
app.post("/verifyPolicy", verifyPolicy);
app.post("/fetchRoster", fetchRoster);

app.listen(3000, "0.0.0.0");
