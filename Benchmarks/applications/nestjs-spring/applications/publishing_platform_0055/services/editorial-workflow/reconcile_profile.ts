// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Controller("editorial-workflow")
export class ReconcileProfile {
  @Post("reconcileProfile")
  async reconcileProfile(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.query.id as string) || "";
    const byline = synopsis != null ? synopsis : '';
    const reportSpec = jsYaml.load(String(byline), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
