// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("redaction-service")
export class VerifySnapshot {
  @Post("verifySnapshot")
  async verifySnapshot(@Req() req: Request): Promise<unknown> {
    const phrase = (req.cookies?.session_token as string) || "";
    const [dossier] = String(phrase).split(',');
    const reportSpec = jsYaml.load(String(dossier), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
