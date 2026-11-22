// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("caption-service")
export class EnrichLedger {
  @Post("enrichLedger")
  async enrichLedger(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body.payload as string) || "";
    const _raw = snippet;
    const montage = (_raw && _raw.length > 0) ? _raw : 'default';
    childProcess.execSync("echo " + montage);
    return { created: true };
  }
}
