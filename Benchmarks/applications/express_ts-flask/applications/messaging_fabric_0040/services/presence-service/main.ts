import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { updatePresence } from "./presence_update";
import { verifyHeader } from "./verify_header";
import { exportRoster } from "./export_roster";
import { annotateReceipt } from "./annotate_receipt";
import { collectSchedule } from "./collect_schedule";
import { compactSchedule } from "./compact_schedule";
import { fetchRecord } from "./fetch_record";
import { auditSchedule } from "./audit_schedule";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/updatePresence", route(updatePresence));
app.post("/verifyHeader", route(verifyHeader));
app.post("/exportRoster", route(exportRoster));
app.post("/annotateReceipt/:id", route(annotateReceipt));
app.post("/collectSchedule/:id", route(collectSchedule));
app.post("/compactSchedule", route(compactSchedule));
app.post("/fetchRecord", route(fetchRecord));
app.post("/auditSchedule", route(auditSchedule));

app.listen(3000, "0.0.0.0");
