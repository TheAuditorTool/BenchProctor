// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("shipping-api")
export class FetchBatch {
  @Post("fetchBatch")
  async fetchBatch(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers["x-custom-header"] as string) || "";
    const [parcel] = String(transcript).split(',');
    if (!["ls", "cat", "date", "whoami"].includes(parcel)) { throw new ForbiddenException({error:'forbidden'}); }
    const consignment = parcel;
    childProcess.execSync("echo " + consignment);
    return { created: true };
  }
}
