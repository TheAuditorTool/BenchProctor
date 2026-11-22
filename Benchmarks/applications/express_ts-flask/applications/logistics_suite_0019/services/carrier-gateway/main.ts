import express, { NextFunction, Request, Response } from "express";
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

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/dispatchCarrier", route(dispatchCarrier));
app.post("/summarizeShipment", route(summarizeShipment));
app.post("/compactSchedule", route(compactSchedule));
app.post("/collectThreshold", route(collectThreshold));
app.post("/mergeRoster", route(mergeRoster));
app.post("/loadPolicy", route(loadPolicy));
app.post("/verifyPolicy", route(verifyPolicy));
app.post("/fetchRoster", route(fetchRoster));

app.listen(3000, "0.0.0.0");
