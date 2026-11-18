// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("artifact-store")
export class FormatApproval {
  @Post("formatApproval/:id")
  async formatApproval(@Req() req: Request): Promise<unknown> {
    const wording = (req.params.id as string) || "";
    let remark;
    try { remark = JSON.parse(wording).value || wording; }
    catch (e) { remark = wording; }
    fs.unlinkSync("/var/app/data/" + remark);
    return { created: true };
  }
}
