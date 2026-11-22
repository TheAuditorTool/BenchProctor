// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("archive-store")
export class SummarizeConfig {
  @Post("summarizeConfig")
  async summarizeConfig(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body.payload as string) || "";
    let dossier;
    try { dossier = JSON.parse(phrase).value || phrase; }
    catch (e) { dossier = phrase; }
    net.connect(80, new URL(String(dossier)).hostname);
    return { created: true };
  }
}
