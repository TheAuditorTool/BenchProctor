// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("fx-service")
export class ConvertFx {
  @Post("convertFx")
  async convertFx(@Req() req: Request): Promise<unknown> {
    const ledger = req.body.payments_payload || "";
    fs.unlinkSync("/var/app/data/" + ledger);
    return { created: true };
  }
}
