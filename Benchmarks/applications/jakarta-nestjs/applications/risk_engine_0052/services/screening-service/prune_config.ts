// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("screening-service")
export class PruneConfig {
  @Post("pruneConfig")
  async pruneConfig(@Req() req: Request): Promise<unknown> {
    const memo = (req.cookies?.session_token as string) || "";
    const [verdict] = String(memo).split(',');
    const reportSpec = jsYaml.load(String(verdict), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
