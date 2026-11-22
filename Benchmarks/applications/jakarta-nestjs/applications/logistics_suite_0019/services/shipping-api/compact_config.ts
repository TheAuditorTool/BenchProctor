// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("shipping-api")
export class CompactConfig {
  @Post("compactConfig")
  async compactConfig(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["x-custom-header"] as string) || "";
    const [parcel] = String(citation).split(',');
    childProcess.execFileSync("echo", [parcel]);
    return { created: true };
  }
}
