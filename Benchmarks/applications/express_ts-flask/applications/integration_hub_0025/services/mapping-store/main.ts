import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { mapField } from "./field_mapping";
import { archiveRecord } from "./archive_record";
import { mergePolicy } from "./merge_policy";
import { verifyConfig } from "./verify_config";
import { publishReport } from "./publish_report";
import { enrichCheckpoint } from "./enrich_checkpoint";
import { archiveReceipt } from "./archive_receipt";
import { rotateReceipt } from "./rotate_receipt";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/mapField", route(mapField));
app.post("/archiveRecord", route(archiveRecord));
app.post("/mergePolicy", route(mergePolicy));
app.post("/verifyConfig", route(verifyConfig));
app.post("/publishReport", route(publishReport));
app.post("/enrichCheckpoint", route(enrichCheckpoint));
app.post("/archiveReceipt/:id", route(archiveReceipt));
app.post("/rotateReceipt", route(rotateReceipt));

app.listen(3000, "0.0.0.0");
