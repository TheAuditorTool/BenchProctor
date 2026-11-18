// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("partner-registry")
export class CompactConfig {
  @Post("compactConfig")
  async compactConfig(@Req() req: Request): Promise<unknown> {
    const quotation = process.env.INTEGRATIONS_INPUT_0001 || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(quotation);
    fs.unlinkSync("/var/app/data/" + handshake);
    return { created: true };
  }
}
