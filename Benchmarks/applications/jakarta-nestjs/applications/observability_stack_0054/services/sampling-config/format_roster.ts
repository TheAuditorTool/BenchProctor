// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("sampling-config")
export class FormatRoster {
  @Post("formatRoster")
  async formatRoster(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.cookies?.session_token as string) || "";
    const [cohort] = String(excerpt).split(',');
    const reportSpec = jsYaml.load(String(cohort), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
