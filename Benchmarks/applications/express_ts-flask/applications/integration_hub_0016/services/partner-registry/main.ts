import express, { Request, Response } from "express";
import session from "express-session";

import { registerPartner } from "./partner_register";
import { renderWebhook } from "./render_webhook";
import { pruneCheckpoint } from "./prune_checkpoint";
import { rotateDigest } from "./rotate_digest";
import { compactPolicy } from "./compact_policy";
import { renderWindow } from "./render_window";
import { loadSchedule } from "./load_schedule";
import { pruneBatch } from "./prune_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/registerPartner", registerPartner);
app.post("/renderWebhook", renderWebhook);
app.post("/pruneCheckpoint", pruneCheckpoint);
app.post("/rotateDigest", rotateDigest);
app.post("/compactPolicy", compactPolicy);
app.post("/renderWindow", renderWindow);
app.post("/loadSchedule/:id", loadSchedule);
app.post("/pruneBatch", pruneBatch);

app.listen(3000, "0.0.0.0");
