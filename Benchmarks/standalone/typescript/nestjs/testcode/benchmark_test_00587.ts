// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00587")
  async BenchmarkTest00587(@Req() req: Request): Promise<unknown> {
    const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const data = `${userInput}`;
    const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
    req.session.data = String(processed);
    return { created: true };
  }
}
