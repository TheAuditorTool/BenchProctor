import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { registerService } from "./service_register";
import { publishSnapshot } from "./publish_snapshot";
import { loadRecord } from "./load_record";
import { resolveBundle } from "./resolve_bundle";
import { rotateRecord } from "./rotate_record";
import { publishCheckpoint } from "./publish_checkpoint";
import { collectReport } from "./collect_report";
import { loadReceipt } from "./load_receipt";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/registerService", route(registerService));
app.post("/publishSnapshot", route(publishSnapshot));
app.post("/loadRecord", route(loadRecord));
app.post("/resolveBundle", route(resolveBundle));
app.post("/rotateRecord", route(rotateRecord));
app.post("/publishCheckpoint", route(publishCheckpoint));
app.post("/collectReport/:id", route(collectReport));
app.post("/loadReceipt/:id", route(loadReceipt));

app.listen(3000, "0.0.0.0");
