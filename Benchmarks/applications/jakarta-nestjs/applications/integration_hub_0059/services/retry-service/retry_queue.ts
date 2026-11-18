// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("retry-service")
export class QueueRetry {
  @Post("queueRetry")
  async queueRetry(@Req() req: Request): Promise<unknown> {
    const remark = req.body.integrations_payload || "";
    if (!/^(asc|desc|name|created)$/.test(String(remark))) { throw new BadRequestException({error:"invalid"}); }
    const memo = remark;
    const fileContent = fs.readFileSync("/var/app/data/" + memo, "utf8");
    return fileContent;
  }
}
