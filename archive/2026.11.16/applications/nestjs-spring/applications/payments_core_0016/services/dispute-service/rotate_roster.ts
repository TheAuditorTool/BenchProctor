// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("dispute-service")
export class RotateRoster {
  @Post("rotateRoster")
  async rotateRoster(@Req() req: Request): Promise<unknown> {
    const passage = process.env.PAYMENTS_INPUT_0016 || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const remittance: string = normalize(passage);
    fs.unlinkSync("/var/app/data/" + remittance);
    return { created: true };
  }
}
