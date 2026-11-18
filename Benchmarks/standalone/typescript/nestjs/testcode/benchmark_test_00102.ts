// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Redirect } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00102")
  @Redirect()
  async BenchmarkTest00102(): Promise<unknown> {
    const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    let data;
    try { data = JSON.parse(userInput).value || ""; }
    catch (e) { data = String(userInput); }
    return { url: data };
  }
}
