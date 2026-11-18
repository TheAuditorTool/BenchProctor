// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, Res } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00626")
  async BenchmarkTest00626(@Body("field") field: string, @Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = field || "";
    const data = String(userInput).replace(/\u0000/g, "");
    res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
    return { created: true };
  }
}
