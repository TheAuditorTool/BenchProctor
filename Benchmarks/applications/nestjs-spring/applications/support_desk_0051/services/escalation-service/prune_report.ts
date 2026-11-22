// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Controller("escalation-service")
export class PruneReport {
  @Post("pruneReport")
  async pruneReport(@Req() req: Request): Promise<unknown> {
    const preface = (req.query.id as string) || "";
    const grievance = preface != null ? preface : '';
    const reportSpec = jsYaml.load(String(grievance), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
