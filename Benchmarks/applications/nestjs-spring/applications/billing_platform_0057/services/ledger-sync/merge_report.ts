// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("ledger-sync")
export class MergeReport {
  @Post("mergeReport")
  async mergeReport(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.payload as string) || "";
    let remittance;
    try { remittance = JSON.parse(caption).value || caption; }
    catch (e) { remittance = caption; }
    net.connect(80, new URL(String(remittance)).hostname);
    return { created: true };
  }
}
