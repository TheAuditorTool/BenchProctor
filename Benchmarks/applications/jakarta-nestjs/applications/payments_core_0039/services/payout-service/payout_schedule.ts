// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payout-service")
export class SchedulePayout {
  @Post("schedulePayout")
  async schedulePayout(@Req() req: Request): Promise<unknown> {
    const disbursement = req.body.payments_payload || "";
    childProcess.execSync("echo " + disbursement);
    return { created: true };
  }
}
