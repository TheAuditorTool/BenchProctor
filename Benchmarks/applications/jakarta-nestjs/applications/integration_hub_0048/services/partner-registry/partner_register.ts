// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("partner-registry")
export class RegisterPartner {
  @Post("registerPartner")
  async registerPartner(@Req() req: Request): Promise<unknown> {
    const preface = req.body.integrations_payload || "";
    fs.writeFileSync("/var/uploads/" + preface, "data");
    return { created: true };
  }
}
