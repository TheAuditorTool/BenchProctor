// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("metrics-ingest")
export class FormatHeader {
  @Post("formatHeader")
  async formatHeader(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers["x-custom-header"] as string) || "";
    const _raw = caption;
    const gauge = (_raw && _raw.length > 0) ? _raw : 'default';
    fs.writeFileSync("/var/uploads/" + gauge, "data");
    return { created: true };
  }
}
