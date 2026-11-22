// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("sla-monitor")
export class PruneReceipt {
  @Post("pruneReceipt/:id")
  async pruneReceipt(@Req() req: Request): Promise<unknown> {
    const phrase = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const grievance: string = normalize(phrase);
    const fileContent = fs.readFileSync("/var/app/data/" + grievance, "utf8");
    return fileContent;
  }
}
