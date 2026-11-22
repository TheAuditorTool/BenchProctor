import express, { Request, Response } from "express";
import session from "express-session";

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
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/registerService", registerService);
app.post("/publishSnapshot", publishSnapshot);
app.post("/loadRecord", loadRecord);
app.post("/resolveBundle", resolveBundle);
app.post("/rotateRecord", rotateRecord);
app.post("/publishCheckpoint", publishCheckpoint);
app.post("/collectReport", collectReport);
app.post("/loadReceipt", loadReceipt);

app.listen(3000, "0.0.0.0");
